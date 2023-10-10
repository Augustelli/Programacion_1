import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ClasesComponent } from './pages/clases/clases.component';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { InicioComponent } from './pages/inicio/inicio.component';
import { EditarPerfilComponent } from './pages/editar-perfil/editar-perfil.component';
import { CrearUsuarioComponent } from './pages/crear-usuario/crear-usuario.component';
// import { CrearUsuarioMainComponent } from './pages/crar-usuario-main/crar-usuario-main.component';
import { LoginTwoComponent } from './pages/login-two/login-two.component';
import { LogoutComponent } from './pages/logout/logout.component';
import { ErrorPageComponent } from './pages/error-page/error-page.component';
import { UsuarioComponent } from './pages/usuario/usuario.component';
import { PayComponent } from './pages/pay/pay.component';
import { UsuariosComponent } from './pages/usuarios/usuarios.component';
import { authsessionGuardToken, authsessionGuardTokenAdminProfe, authsessionGuardTokenAdminProfeAlum, authsessionGuardTokenAdminProfeAlumEspera, authsessionGuardTokenAdmin } from './guards/authsession.guard';
import { CrearUsuarioAdminComponent } from './pages/crear-usuario-admin/crear-usuario-admin.component';



const routes: Routes = [
  {path:'',redirectTo:'/inicio',pathMatch:'full'},
  {path:'inicio',component:InicioComponent},
  {path:'home',component:HomeComponent},
  {path:'login',component:LoginComponent},
  {path:'clases',component:ClasesComponent},
  // {path:'**',redirectTo:'error_page'},
  {path:'editar_perfil',component:EditarPerfilComponent, canActivate:[authsessionGuardTokenAdminProfeAlum]},
  {path:'crear_usuario',component:CrearUsuarioComponent},
  {path:'login_two',component:LoginTwoComponent},
  {path:'logout',component:LogoutComponent, canActivate:[authsessionGuardTokenAdminProfeAlumEspera]},
  {path:'error_page',component:ErrorPageComponent},
  {path:'usuarios',component:UsuariosComponent, canActivate:[authsessionGuardTokenAdminProfe]},
  {path:'pay',component:PayComponent, canActivate:[authsessionGuardTokenAdminProfeAlum]},
  { path: 'usuario/:id/:tipo_op', component: UsuarioComponent, canActivate:[authsessionGuardTokenAdminProfe]},
  { path: 'crear_usuario_admin', component: CrearUsuarioAdminComponent , canActivate:[authsessionGuardTokenAdminProfe]},
  
  // {path:'crear_usuario_main',component:CrearUsuarioMainComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
