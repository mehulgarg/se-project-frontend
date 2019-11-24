import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModuleCardComponent } from './module-card.component';

describe('ModuleCardComponent', () => {
  let component: ModuleCardComponent;
  let fixture: ComponentFixture<ModuleCardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModuleCardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModuleCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
