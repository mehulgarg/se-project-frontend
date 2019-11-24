import { Component, OnInit, OnDestroy, ChangeDetectionStrategy, ChangeDetectorRef } from '@angular/core';
import { ModuleContentService } from 'src/app/shared/services/module-content.service';
import { ActivatedRoute, Router } from '@angular/router';
import { AppConstants } from 'src/assets/app_constants';

@Component({
  selector: 'app-module-content',
  templateUrl: './module-content.component.html',
  styleUrls: ['./module-content.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ModuleContentComponent implements OnInit {

  moduleHeading;
  frameworkName;
  data;
  prevroute;
  constructor(private activatedRoute: ActivatedRoute, private changeDetector: ChangeDetectorRef, private router: Router) {
    this.activatedRoute.params.subscribe(params => this.frameworkName = params.frameworkName);
  }

  ngOnInit() {
    this.moduleHeading = '';
    this.data = [];
    this.changeDetector.detectChanges();
    console.log(sessionStorage.getItem(AppConstants.MODULE_NAME));
    this.moduleHeading = sessionStorage.getItem(AppConstants.MODULE_NAME);
    console.log(sessionStorage.getItem(sessionStorage.getItem(AppConstants.MODULE_DATA)));
    this.data = JSON.parse(sessionStorage.getItem(AppConstants.MODULE_DATA));
    this.changeDetector.detectChanges();
  }

  navigateToFrameworkModules() {
    this.router.navigate([sessionStorage.getItem(AppConstants.PREV_ROUTE)]);
  }
}
