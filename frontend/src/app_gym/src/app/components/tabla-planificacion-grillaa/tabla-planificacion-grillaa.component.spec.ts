import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TablaPlanificacionGrillaaComponent } from './tabla-planificacion-grillaa.component';

describe('TablaPlanificacionGrillaaComponent', () => {
  let component: TablaPlanificacionGrillaaComponent;
  let fixture: ComponentFixture<TablaPlanificacionGrillaaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TablaPlanificacionGrillaaComponent]
    });
    fixture = TestBed.createComponent(TablaPlanificacionGrillaaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
