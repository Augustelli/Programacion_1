import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Backvar2Component } from './backvar2.component';

describe('Backvar2Component', () => {
  let component: Backvar2Component;
  let fixture: ComponentFixture<Backvar2Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [Backvar2Component]
    });
    fixture = TestBed.createComponent(Backvar2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
