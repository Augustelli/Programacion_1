import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { ClasesComponent } from './pages/clases/clases.component';
import { ErrorPageComponent } from './pages/error-page/error-page.component';
import { Nav1Component } from './components/nav1/nav1.component';
import { Nav2Component } from './components/nav2/nav2.component';
import { Backvar1Component } from './components/backvar1/backvar1.component';
import { Backvar2Component } from './components/backvar2/backvar2.component';
import { VerPlanificacionesComponent } from './components/ver-planificaciones/ver-planificaciones.component';
import { VerClasesComponent } from './components/ver-clases/ver-clases.component';
import { InicioComponent } from './pages/inicio/inicio.component';
import { EditarPerfilComponent } from './pages/editar-perfil/editar-perfil.component';
import * as crearUsuarioComponent from './pages/crear-usuario/crear-usuario.component';
import { FlechaAtrasComponent } from './components/flecha-atras/flecha-atras.component';
import { BotonesBkctComponent } from './components/botones-bkct/botones-bkct.component';
import { ScrollNumbersComponent } from './components/scroll-numbers/scroll-numbers.component';
import { TablaPlanificacionComponent } from './components/tabla-planificacion/tabla-planificacion.component';
import { SexoComponent } from './components/sexo/sexo.component';
// import { CrearUsuarioComponent } from './pages/crar-usuario-main/crar-usuario-main.component';
// import MatInputModule from '@angular/material/input';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoginComponent,
    ClasesComponent,
    ErrorPageComponent,
    Nav1Component,
    Nav2Component,
    Backvar1Component,
    Backvar2Component,
    VerPlanificacionesComponent,
    VerClasesComponent,
    InicioComponent,
    EditarPerfilComponent,
    crearUsuarioComponent.CrearUsuarioComponent,
    FlechaAtrasComponent,
    BotonesBkctComponent,
    ScrollNumbersComponent,
    TablaPlanificacionComponent,
    SexoComponent,
    // crearUsuarioComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
