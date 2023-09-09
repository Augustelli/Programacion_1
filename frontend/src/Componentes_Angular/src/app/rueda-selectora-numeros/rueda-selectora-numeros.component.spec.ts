import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RuedaSelectorComponent } from './rueda-selectora-numeros.component';

describe('RuedaSelectoraNumerosComponent', () => {
  let component: RuedaSelectorComponent;
  let fixture: ComponentFixture<RuedaSelectorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [RuedaSelectorComponent]
    });
    fixture = TestBed.createComponent(RuedaSelectorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
