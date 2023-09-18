import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FlechaAtrasComponent } from './flecha-atras.component';

describe('FlechaAtrasComponent', () => {
  let component: FlechaAtrasComponent;
  let fixture: ComponentFixture<FlechaAtrasComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [FlechaAtrasComponent]
    });
    fixture = TestBed.createComponent(FlechaAtrasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
