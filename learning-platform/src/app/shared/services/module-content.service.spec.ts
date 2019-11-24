import { TestBed } from '@angular/core/testing';

import { ModuleContentService } from './module-content.service';

describe('ModuleContentService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ModuleContentService = TestBed.get(ModuleContentService);
    expect(service).toBeTruthy();
  });
});
