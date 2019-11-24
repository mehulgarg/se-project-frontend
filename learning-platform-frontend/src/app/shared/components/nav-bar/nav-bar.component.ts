import { Component, OnInit } from '@angular/core';
import { User } from 'src/app/learning-platform/models/user';
import { AppConstants } from 'src/assets/app_constants';
import { Router } from '@angular/router';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.scss']
})
export class NavBarComponent implements OnInit {

  loggedIn: boolean;
  loggedInUser: User;
  constructor(private router: Router) { }

  ngOnInit() {
    console.log('logged in user', this.loggedInUser);
    this.loggedIn = JSON.parse(sessionStorage.getItem(AppConstants.IS_LOGGEDIN));
    this.loggedInUser = JSON.parse(sessionStorage.getItem(AppConstants.LOGGED_IN_USER));
  }

  logout() {
    console.log('log out clicked');
    sessionStorage.setItem(AppConstants.IS_LOGGEDIN, 'false');
    sessionStorage.removeItem(AppConstants.LOGGED_IN_USER);
    sessionStorage.removeItem(AppConstants.TEXT_EDITOR_STARTED);
    sessionStorage.removeItem(AppConstants.DEPLOYMENT_SERVER_STARTED);
    sessionStorage.removeItem(AppConstants.TEXT_EDITOR_PASSWORD);
    sessionStorage.removeItem(AppConstants.TEXT_EDITOR_URL);
    sessionStorage.removeItem(AppConstants.DEPLOYMENT_SERVER_URL);
    this.router.navigate(['/login']);
  }

}
