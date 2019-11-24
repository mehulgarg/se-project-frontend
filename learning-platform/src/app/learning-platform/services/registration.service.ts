import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { throwError, BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RegistrationService {

  registerErrorSubject = new BehaviorSubject<string>(null);
  // serverUrl = 'http://127.0.0.1/register';
  serverUrl = 'http://192.168.43.144/signup';
  // serverUrl = 'http://192.168.43.20/signup';
  constructor(private httpClient: HttpClient) { }

  register(userData) {
    return this.httpClient.post<any>(this.serverUrl, {
      email: userData.email,
      password: userData.password,
      fullName: userData.fullName
    })
    .pipe(catchError(this.errorHandler));
  }
  errorHandler(error: HttpErrorResponse) {
    console.log('error handler in service');
    this.registerErrorSubject.next(error.toString());
    return throwError(error);
  }
}
