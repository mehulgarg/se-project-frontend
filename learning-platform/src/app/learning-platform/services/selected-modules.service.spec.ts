import { TestBed } from '@angular/core/testing';

import { SelectedModulesService } from './selected-modules.service';

describe('SelectedModulesService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: SelectedModulesService = TestBed.get(SelectedModulesService);
    expect(service).toBeTruthy();
  });
});
