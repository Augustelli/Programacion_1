import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginTwoComponent } from './login-two.component';

describe('LoginTwoComponent', () => {
  let component: LoginTwoComponent;
  let fixture: ComponentFixture<LoginTwoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [LoginTwoComponent]
    });
    fixture = TestBed.createComponent(LoginTwoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
