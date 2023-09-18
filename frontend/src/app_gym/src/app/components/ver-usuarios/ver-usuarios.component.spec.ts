import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VerUsuariosComponent } from './ver-usuarios.component';

describe('VerUsuariosComponent', () => {
  let component: VerUsuariosComponent;
  let fixture: ComponentFixture<VerUsuariosComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [VerUsuariosComponent]
    });
    fixture = TestBed.createComponent(VerUsuariosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
