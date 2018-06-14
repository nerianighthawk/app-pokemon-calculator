import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CalcuratorComponent } from './calcurator.component';

describe('CalcuratorComponent', () => {
  let component: CalcuratorComponent;
  let fixture: ComponentFixture<CalcuratorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CalcuratorComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CalcuratorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
