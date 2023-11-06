import { Component } from '@angular/core';


@Component({
  selector: 'app-flecha-atras',
  template: `
    <nav class="navbar bg-body-tertiary" style="
    background-color: #d8e7f7; 
    background-size: cover;         
    margin: 0;       
    padding: 0;">
      <div class="container-fluid" style="
      background-color: #d8e7f7; 
      background-size: cover;         
      margin: 0;       
      padding: 0;">
        <a class="navbar-brand" href="javascript:void(0)" (click)="back()" role="button">
          <div>
            <img src="../../assets/back.svg" alt="configuracion" width="30" height="24" class="d-inline-block align-text-top">
          </div>
        </a>
      </div>
    </nav>
  `,
  styles: []
})
export class FlechaAtrasComponent {
  constructor() {}
  

  back() {
    window.history.back();
  }
}