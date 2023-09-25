import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Backvar1Component } from './backvar1.component';

describe('Backvar1Component', () => {
  let component: Backvar1Component;
  let fixture: ComponentFixture<Backvar1Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [Backvar1Component]
    });
    fixture = TestBed.createComponent(Backvar1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
