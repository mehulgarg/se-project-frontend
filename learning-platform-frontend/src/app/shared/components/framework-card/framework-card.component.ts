import { Component, OnInit, Input, ChangeDetectorRef, ChangeDetectionStrategy, NgZone } from '@angular/core';
import { User } from 'src/app/learning-platform/models/user';
import { AppConstants } from 'src/assets/app_constants';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-framework-card',
  templateUrl: './framework-card.component.html',
  styleUrls: ['./framework-card.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class FrameworkCardComponent implements OnInit {

  @Input() framework;
  loggedInUser: User;
  hasSignedUp: boolean;
  loadingClicked;
  initFramework;
  error: boolean;
  frameworkId;
  frameworkName;
  // frameworkDataUrl = 'http://127.0.0.1:5000/hassignedup';
  // initializeUrl = 'http://127.0.0.1:5000/initialize';
  frameworkDataUrl = 'http://192.168.43.144/framework_signup_exists';
  initializeUrl = 'http://192.168.43.144/framework_signup';
  // frameworkDataUrl = 'http://192.168.43.20/framework_signup_exists';
  // initializeUrl = 'http://192.168.43.20/framework_signup';
  constructor(private http: HttpClient, private router: Router, private changeDetector: ChangeDetectorRef, private zone: NgZone, ) { }

  ngOnInit() {
    console.log('init called');
    this.loggedInUser = JSON.parse(sessionStorage.getItem(AppConstants.LOGGED_IN_USER));
    this.loadingClicked = false;
    this.initFramework = false;
    this.hasSignedUp = false;
    this.changeDetector.markForCheck();
    console.log('logged in user', this.loggedInUser);
    this.http.get<any>(this.frameworkDataUrl, {
      params: {
        email: this.loggedInUser.email,
        frameworkId: this.framework.frameworkName.toString().toLowerCase(),
      }
    }).subscribe(
      data => {
        console.log(this.framework.frameworkName, 'signed up for');
        this.hasSignedUp = true;
        this.changeDetector.detectChanges();
      },
      error => {
        this.hasSignedUp = false;
        console.log(error);
      }
    );
  }
  navigateToModules(frameworkId, frameworkName) {
    this.frameworkId = frameworkId;
    this.frameworkName = frameworkName;
    if (this.hasSignedUp) {
      this.moveToModules();
    } else {
      this.initialize();
    }
  }

  moveToModules() {
    this.router.navigate(['/frameworks', this.frameworkId, this.frameworkName]);
  }

  initialize() {
    console.log('in initialize');
    this.httpInit();
  }

  httpInit() {
    this.loadingClicked = true;
    this.zone.run(() => {
      this.http.post<any>(this.initializeUrl, {
          email: this.loggedInUser.email,
          frameworkName: this.framework.frameworkName.toString().toLowerCase(),
      }).subscribe(
        data => {
          console.log(data);
          this.zone.run(() => {
            console.log('true');
            this.initFramework = true;
            this.error = false;
            this.changeDetector.detectChanges();
          });
        },
        error => {
          this.initFramework = true;
          this.zone.run(() => {
            console.log('true');
            this.initFramework = true;
            this.error = true;
            this.changeDetector.detectChanges();
          });
        });
    });
  }

  tryAgain() {
    console.log('try again');
    this.zone.run(() => {
      this.loadingClicked = true;
      this.initFramework = false;
      this.changeDetector.detectChanges();
      this.httpInit();
    });
  }
}
