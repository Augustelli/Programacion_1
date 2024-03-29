import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { ClasesComponent } from './pages/clases/clases.component';
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
import { SexoComponent } from './components/sexo/sexo.component';
import { TablaPlanificacionGrillaaComponent } from './components/tabla-planificacion-grillaa/tabla-planificacion-grillaa.component';
import { LoginTwoComponent } from './pages/login-two/login-two.component';
import { LoginThreeComponent } from './components/login-three/login-three.component';
import { LogoutComponent } from './pages/logout/logout.component';
import { UsuarioComponent } from './pages/usuario/usuario.component';
import { VerUsuariosComponent } from './components/ver-usuarios/ver-usuarios.component';
import { PayComponent } from './pages/pay/pay.component';
import { UsuariosComponent } from './pages/usuarios/usuarios.component';
import { AbmComponent } from './components/abm/abm.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import {JwtModule} from '@auth0/angular-jwt';
import { CrearUsuarioAdminComponent } from './pages/crear-usuario-admin/crear-usuario-admin.component';
import { NgxPaginationModule } from 'ngx-pagination';
import { ToastrModule } from 'ngx-toastr';
import { PayAdminComponent } from './pages/pay-admin/pay-admin.component';
import { ProfesComponent } from './pages/profes/profes.component';
import { CommonModule } from '@angular/common';

 

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
  
    ClasesComponent,
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
    SexoComponent,
    LoginTwoComponent,
    LogoutComponent,
    UsuarioComponent,
    VerUsuariosComponent,
    PayComponent,
    UsuariosComponent,
    AbmComponent,
    CrearUsuarioAdminComponent,
    PayAdminComponent,
    ProfesComponent,
    TablaPlanificacionGrillaaComponent,

  ],
  imports: [
    BrowserModule,
    CommonModule,
    FormsModule,
    CommonModule,
    AppRoutingModule,
    LoginThreeComponent,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    NgxPaginationModule,
    ToastrModule.forRoot(),
    JwtModule.forRoot({
      config: {
        tokenGetter: () => {
          return localStorage.getItem('tu_variable_token');
        },
        allowedDomains: ['example.com'],
      },
    }),

  
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
