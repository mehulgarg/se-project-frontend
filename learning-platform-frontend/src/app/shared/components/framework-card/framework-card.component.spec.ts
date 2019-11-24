import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FrameworkCardComponent } from './framework-card.component';

describe('FrameworkCardComponent', () => {
  let component: FrameworkCardComponent;
  let fixture: ComponentFixture<FrameworkCardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FrameworkCardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FrameworkCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
