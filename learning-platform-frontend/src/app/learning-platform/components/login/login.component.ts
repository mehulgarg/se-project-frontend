import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { LoginService } from '../../services/login.service';
import { Router } from '@angular/router';
import { User } from '../../models/user';
import { AppConstants } from 'src/assets/app_constants';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  form: FormGroup;
  error: boolean;
  get userEmail() {
    return this.form.get('email');
  }
  constructor(private formBuilder: FormBuilder, private loginService: LoginService, private router: Router, ) {
    this.loginService.isLoggedIn = JSON.parse(sessionStorage.getItem(AppConstants.IS_LOGGEDIN));
    this.loginService.loggedInUser = JSON.parse(sessionStorage.getItem(AppConstants.LOGGED_IN_USER));
  }

  ngOnInit() {
    this.form = this.formBuilder.group({
      email: [null, [Validators.required, Validators.email]],
      password: [null, Validators.required],
    });

    if (this.loginService.isLoggedIn) {
      this.router.navigate(['/home']);
    }
    this.error = false;
  }

  onSubmit() {
    console.log('login form submitted ', this.form.value);
    this.loginService.login(this.form.value)
      .subscribe(
        response => this.confirmLogin(response),
        error => this.handleLoginError(error),
      );
  }
  confirmLogin(response) {
    console.log('Response ', response);
    sessionStorage.setItem(AppConstants.IS_LOGGEDIN, 'true');
    sessionStorage.setItem(AppConstants.LOGGED_IN_USER, JSON.stringify(response));
    this.loginService.isLoggedIn = true;
    this.loginService.loggedInUser = response;
    this.router.navigate(['/home']);
  }

  handleLoginError(error) {
    console.log('error in component', error);
    this.loginService.logInErrorSubject.subscribe(
      next => {
        console.log('test in subject');
        this.error = true;
      });
  }
}
