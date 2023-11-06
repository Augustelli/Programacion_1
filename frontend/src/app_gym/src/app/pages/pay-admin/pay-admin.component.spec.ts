import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PayAdminComponent } from './pay-admin.component';

describe('PayAdminComponent', () => {
  let component: PayAdminComponent;
  let fixture: ComponentFixture<PayAdminComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PayAdminComponent]
    });
    fixture = TestBed.createComponent(PayAdminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
