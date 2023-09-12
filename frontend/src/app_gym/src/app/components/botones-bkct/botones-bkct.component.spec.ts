import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BotonesBkctComponent } from './botones-bkct.component';

describe('BotonesBkctComponent', () => {
  let component: BotonesBkctComponent;
  let fixture: ComponentFixture<BotonesBkctComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BotonesBkctComponent]
    });
    fixture = TestBed.createComponent(BotonesBkctComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
