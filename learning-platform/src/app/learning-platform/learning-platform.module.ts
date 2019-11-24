import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LearningPlatformRoutingModule, routingComponents } from './learning-platform-routing.module';
import { DemoMaterialModule } from '../core/material-module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

import { NavBarComponent } from '../../app/shared/components/nav-bar/nav-bar.component';
import { FrameworkCardComponent } from '../../app/shared/components/framework-card/framework-card.component';
import { ModuleCardComponent } from '../../app/shared/components/module-card/module-card.component';

@NgModule({
  declarations:
    [
      routingComponents,
      NavBarComponent,
      FrameworkCardComponent,
      ModuleCardComponent,
    ],
  imports: [
    LearningPlatformRoutingModule,
    CommonModule,
    DemoMaterialModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule,
    HttpClientModule
  ]
})
export class LearningPlatformModule { }
