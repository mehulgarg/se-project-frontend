import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
// import {} from ''


const routes: Routes = [
  {path: '',
  loadChildren: () => import('./learning-platform/learning-platform.module').then(mod => mod.LearningPlatformModule)}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
