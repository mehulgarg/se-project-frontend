import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { HomepageComponent } from './components/homepage/homepage.component';
import { FrameworksComponent } from './components/frameworks/frameworks.component';
import { IndividualFrameworkComponent} from './components/individual-framework/individual-framework.component';
import { ModuleContentComponent } from './components/module-content/module-content.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'home', component: HomepageComponent},
  { path: 'frameworks', component: FrameworksComponent },
  { path: 'frameworks/:frameworkId/:frameworkName', component: IndividualFrameworkComponent },
  { path: 'modules/:frameworkName/:moduleNumber', component: ModuleContentComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];
@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LearningPlatformRoutingModule {
  constructor() {
    console.log('test');
  }
}

export const routingComponents = [
                                  LoginComponent,
                                  RegisterComponent,
                                  HomepageComponent,
                                  FrameworksComponent,
                                  IndividualFrameworkComponent,
                                  ModuleContentComponent
                                 ];
