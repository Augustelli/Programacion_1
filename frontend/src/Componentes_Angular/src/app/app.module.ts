import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RuedaSelectorComponent } from './rueda-selectora-numeros/rueda-selectora-numeros.component';

@NgModule({
  declarations: [
    AppComponent,
    RuedaSelectorComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
