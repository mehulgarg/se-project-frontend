import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { throwError, BehaviorSubject, } from 'rxjs';
import { User } from '../models/user';

@Injectable({
  providedIn: 'root'
})

export class LoginService {

  isLoggedIn = false;
  loggedInUser: User;

  // serverUrl = 'http://127.0.0.1:5000/login';
  serverUrl = 'http://192.168.43.144/login';
  // serverUrl = 'http://192.168.43.20/login';
  logInErrorSubject = new BehaviorSubject<string>(null);
  constructor(private httpClient: HttpClient) {
  }

  login(userData) {
    console.log('data in service', userData);
    return this.httpClient.post<User>(this.serverUrl, userData).
    pipe(catchError((error) => this.errorHandler(error)));
  }
  errorHandler(error: HttpErrorResponse) {
    console.log('error in service', error);
    this.logInErrorSubject.next(error.toString());
    return throwError(error);
  }
}
