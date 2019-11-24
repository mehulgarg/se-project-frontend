import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IndividualFrameworkComponent } from './individual-framework.component';

describe('IndividualFrameworkComponent', () => {
  let component: IndividualFrameworkComponent;
  let fixture: ComponentFixture<IndividualFrameworkComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IndividualFrameworkComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IndividualFrameworkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
