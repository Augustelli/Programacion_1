import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TablaPlanificacion } from './tabla-planificacion.component';

describe('TablaPlanificacionComponent', () => {
  let component: TablaPlanificacion;
  let fixture: ComponentFixture<TablaPlanificacion>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TablaPlanificacion]
    });
    fixture = TestBed.createComponent(TablaPlanificacion);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
