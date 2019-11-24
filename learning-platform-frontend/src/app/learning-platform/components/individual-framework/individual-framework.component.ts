import { Component, OnInit, ChangeDetectionStrategy, ChangeDetectorRef } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { IndividualFramework } from '../../models/individual-framework';
import { AppConstants } from 'src/assets/app_constants';
import { User } from '../../models/user';

@Component({
  selector: 'app-individual-framework',
  templateUrl: './individual-framework.component.html',
  styleUrls: ['./individual-framework.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class IndividualFrameworkComponent implements OnInit {

  frameworkId: number;
  frameworkName: string;
  individualFramework: IndividualFramework;
  individualModules;

  startTextEditorClicked: boolean;
  textEditorButton: boolean;
  successTextEditor: boolean;
  textEditorUrl: string;
  passwordTextEditorSuccess: boolean;
  passwordTextEditor: string;

  startDeploymentServerClicked: boolean;
  deploymentServerButton: boolean;
  successDeploymentServer: boolean;
  deploymentServerUrl: string;

  loggedInUser: User;

  // contentsUrl = 'http://127.0.0.1:5000/frameworkContents';
  // startTextEditorUrl = 'http://127.0.0.1:5000/start-text-editor';
  // startDeploymentServerUrl = 'http://127.0.0.1:5000/deploy_server';
  // textEditorPasswordUrl = 'http://127.0.0.1:5000/password_text_editor';
  // backendIp = 'http://127.0.0.1:5000/';
  backendIp = 'http://192.168.43.144/';
  // backendIp = 'http://192.168.43.20/';
  contentsUrl = 'http://127.0.0.1:5000/frameworkContents';
  startTextEditorUrl = this.backendIp + 'code_editor';
  startDeploymentServerUrl = this.backendIp + 'deploy_server';
  textEditorPasswordUrl = this.backendIp + 'code_editor_password';

  constructor(private route: ActivatedRoute, private http: HttpClient, private changeDectector: ChangeDetectorRef) {
    this.route.params.subscribe(params => { this.frameworkId = params.frameworkId, this.frameworkName = params.frameworkName; });
    this.loggedInUser = JSON.parse(sessionStorage.getItem(AppConstants.LOGGED_IN_USER));
  }


  ngOnInit() {
    this.startTextEditorClicked = false;
    this.individualModules = [];
    this.textEditorButton = true;
    this.successTextEditor = sessionStorage.getItem(AppConstants.TEXT_EDITOR_STARTED) === 'true';
    this.passwordTextEditorSuccess = sessionStorage.getItem(AppConstants.TEX_EDITOR_PASSWORD_RECEIVED) === 'true';
    this.passwordTextEditor = sessionStorage.getItem(AppConstants.TEXT_EDITOR_PASSWORD);

    this.startDeploymentServerClicked = false;
    this.deploymentServerButton = true;
    this.successDeploymentServer = sessionStorage.getItem(AppConstants.DEPLOYMENT_SERVER_STARTED) === 'true';

    this.changeDectector.detectChanges();

    console.log(this.frameworkId);
    this.http.get<any>(this.contentsUrl, {
      params: {
        frameworkId: this.frameworkId.toString(),
      }
    }).subscribe(
      data => {
        // this.individualFramework = data;
        console.log(JSON.stringify(data));
        this.individualFramework = JSON.parse(JSON.parse(JSON.stringify(data)));
        console.log(this.individualFramework, typeof (this.individualFramework));
        console.log(this.individualFramework.modules);
        this.individualModules = this.individualFramework.modules;
        this.changeDectector.detectChanges();
        console.log(this.individualModules);
      }
    );
  }

  startTextEditor() {
    this.successTextEditor = sessionStorage.getItem(AppConstants.TEXT_EDITOR_STARTED) === 'true';
    if (!this.successTextEditor) {
      this.startTextEditorClicked = true;
      this.changeDectector.detectChanges();
      this.http.put<any>(this.startTextEditorUrl, {
        email: this.loggedInUser.email,
        frameworkId: this.frameworkName.toLowerCase(),
      }).subscribe(
        data => {
          this.textEditorButton = true;
          this.startTextEditorClicked = false;
          sessionStorage.setItem(AppConstants.TEXT_EDITOR_STARTED, 'true');
          this.successTextEditor = sessionStorage.getItem(AppConstants.TEXT_EDITOR_STARTED) === 'true';
          this.changeDectector.detectChanges();
          this.textEditorUrl = 'http://' + JSON.parse(data);
          sessionStorage.setItem(AppConstants.TEXT_EDITOR_URL, this.textEditorUrl);
          this.getTextEditorPassword();
          this.openTextEditorWindow();
        },
        error => {
          this.textEditorButton = false;
          this.startTextEditorClicked = false;
          this.changeDectector.detectChanges();
        });
    } else {
      this.openTextEditorWindow();
    }
  }


  getTextEditorPassword() {
    this.http.get<any>(this.textEditorPasswordUrl, {
      params: {
        email: this.loggedInUser.email,
        frameworkId: this.frameworkName.toLowerCase(),
      }
    }).subscribe(
      data => {
        sessionStorage.setItem(AppConstants.TEX_EDITOR_PASSWORD_RECEIVED, 'true');
        sessionStorage.setItem(AppConstants.TEXT_EDITOR_PASSWORD, JSON.parse(data).password);
        this.passwordTextEditor = sessionStorage.getItem(AppConstants.TEXT_EDITOR_PASSWORD);
        this.passwordTextEditorSuccess = true;
        this.changeDectector.detectChanges();
      },
      error => {
        console.log(error);
      }
    );
  }
  openTextEditorWindow() {
    window.open(sessionStorage.getItem(AppConstants.TEXT_EDITOR_URL));
  }
  stopTextEditor() {
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
      body: {
        email: this.loggedInUser.email,
        frameworkId: this.frameworkName.toLowerCase(),
      }
    };
    this.http.delete<any>(this.startTextEditorUrl, options).subscribe(
      data => {
        console.log(data);
        this.successTextEditor = false;
        this.textEditorButton = true;
        this.passwordTextEditorSuccess = false;
        this.passwordTextEditor = '';
        sessionStorage.setItem(AppConstants.TEXT_EDITOR_STARTED, 'false');
        sessionStorage.setItem(AppConstants.TEX_EDITOR_PASSWORD_RECEIVED, 'false');
        sessionStorage.removeItem(AppConstants.TEXT_EDITOR_PASSWORD);
        this.changeDectector.detectChanges();
      },
      error => { console.log(error); this.successTextEditor = true; this.changeDectector.detectChanges(); }
    );
  }


  startDeploymentServer() {
    this.successDeploymentServer = sessionStorage.getItem(AppConstants.DEPLOYMENT_SERVER_STARTED) === 'true';
    if (!this.successDeploymentServer) {
      this.startDeploymentServerClicked = true;
      this.changeDectector.detectChanges();
      this.http.put<any>(this.startDeploymentServerUrl, {
        email: this.loggedInUser.email,
        frameworkId: this.frameworkName.toLowerCase(),
      }).subscribe(
        data => {
          this.deploymentServerButton = true;
          this.startDeploymentServerClicked = false;
          sessionStorage.setItem(AppConstants.DEPLOYMENT_SERVER_STARTED, 'true');
          this.successDeploymentServer = sessionStorage.getItem(AppConstants.DEPLOYMENT_SERVER_STARTED) === 'true';
          this.changeDectector.detectChanges();
          this.deploymentServerUrl = 'http://' + JSON.parse(data);
          sessionStorage.setItem(AppConstants.DEPLOYMENT_SERVER_URL, this.deploymentServerUrl);
          this.openDeploymentServerWindow();
        },
        error => {
          this.deploymentServerButton = false;
          this.startDeploymentServerClicked = false;
          this.changeDectector.detectChanges();
        });
    } else {
      this.openDeploymentServerWindow();
    }
  }

  stopDeploymentServer() {
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
      body: {
        email: this.loggedInUser.email,
        frameworkId: this.frameworkName.toLowerCase(),
      }
    };
    this.http.delete<any>(this.startDeploymentServerUrl, options).subscribe(
      data => {
        console.log(data);
        this.successDeploymentServer = false;
        this.deploymentServerButton = true;
        sessionStorage.setItem(AppConstants.DEPLOYMENT_SERVER_STARTED, 'false');
        this.changeDectector.detectChanges();
      },
      error => { console.log(error); this.deploymentServerButton = true; this.changeDectector.detectChanges(); }
    );
  }

  openDeploymentServerWindow() {
    window.open(sessionStorage.getItem(AppConstants.DEPLOYMENT_SERVER_URL));
  }
}
