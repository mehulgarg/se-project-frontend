import { Injectable } from '@angular/core';
import { Users } from '../models/users';

@Injectable({
  providedIn: 'root'
})
export class SelectedModulesService {

  user: Users = null;
  constructor() {
    this.user = new Users('test');
  }
}
