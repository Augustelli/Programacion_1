import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrarUsuarioMainComponent } from './crar-usuario-main.component';

describe('CrarUsuarioMainComponent', () => {
  let component: CrarUsuarioMainComponent;
  let fixture: ComponentFixture<CrarUsuarioMainComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CrarUsuarioMainComponent]
    });
    fixture = TestBed.createComponent(CrarUsuarioMainComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
