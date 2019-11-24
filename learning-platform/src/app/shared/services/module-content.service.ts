import { Injectable } from '@angular/core';
import { Subject, Observable } from 'rxjs';
import { ModuleServiceContent } from 'src/app/learning-platform/models/module-content-service-model';

@Injectable({
  providedIn: 'root'
})
export class ModuleContentService {

  private moduleContentSubject = new Subject<ModuleServiceContent>();

  constructor() { }

  public addContent(moduleFrameWork, moduleHeading, moduleContentArray) {
    const moduleContent = new ModuleServiceContent();
    moduleContent.moduleFramework = moduleFrameWork;
    moduleContent.moduleHeading = moduleHeading;
    moduleContent.moduleContentArray = moduleContentArray;
    this.moduleContentSubject.next(moduleContent);
  }

  public getData(): Observable<ModuleServiceContent> {
    return this.moduleContentSubject.asObservable();
  }
}
