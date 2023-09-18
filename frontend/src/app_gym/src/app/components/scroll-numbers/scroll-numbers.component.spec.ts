import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ScrollNumbersComponent } from './scroll-numbers.component';

describe('ScrollNumbersComponent', () => {
  let component: ScrollNumbersComponent;
  let fixture: ComponentFixture<ScrollNumbersComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ScrollNumbersComponent]
    });
    fixture = TestBed.createComponent(ScrollNumbersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
