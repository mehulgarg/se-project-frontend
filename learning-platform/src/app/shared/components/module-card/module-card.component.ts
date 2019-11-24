import { Component, OnInit, Input } from '@angular/core';
import { IndividualModule } from 'src/app/learning-platform/models/individual-module';
import { ModuleContentService } from '../../services/module-content.service';
import { Router } from '@angular/router';
import { AppConstants } from 'src/assets/app_constants';

@Component({
  selector: 'app-module-card',
  templateUrl: './module-card.component.html',
  styleUrls: ['./module-card.component.scss']
})
export class ModuleCardComponent implements OnInit {

  @Input() module: IndividualModule;
  @Input() moduleNumber: number;
  @Input() frameworkName: string;
  constructor(private moduleContent: ModuleContentService, private router: Router) {
    console.log('Module details ', this.module);
  }

  ngOnInit() {
    console.log('Module details ', this.module);
  }

  viewModule(moduleName, moduleContent) {
    sessionStorage.setItem(AppConstants.MODULE_NAME, moduleName);
    // console.log(moduleContent);
    sessionStorage.setItem(AppConstants.MODULE_DATA, JSON.stringify(moduleContent));
    console.log(JSON.parse(sessionStorage.getItem(AppConstants.MODULE_DATA)));
    sessionStorage.setItem(AppConstants.PREV_ROUTE, this.router.url);
    this.router.navigate(['/modules', this.frameworkName, this.moduleNumber + 1]);
  }
}
