import { CanActivateFn, Router } from '@angular/router';
import { inject, } from '@angular/core';
import { JwtHelperService, } from '@auth0/angular-jwt';

// import { CanActivateFn, Router } from '@angular/router';
// import { inject,  } from '@angular/core';


export const authsessionGuardToken: CanActivateFn = (route, state) => {
  const router:Router = inject(Router);
  const token = localStorage.getItem('token');
  if (!token) {
    router.navigateByUrl('home');
    return false;
  }else{
  return true;
  }
};


export const authsessionGuardTokenAdminProfe: CanActivateFn = (route, state) => {
  const router:Router = inject(Router);
  const token = localStorage.getItem('token');
  const helper: JwtHelperService = inject(JwtHelperService);
  if (token) {
    const decodedToken = helper.decodeToken(token);
    if (decodedToken.rol === 'admin' || decodedToken.rol === 'profesor'){
      return true;
    }else{
      router.navigateByUrl('home');
      return false;
    }
  } else {
    router.navigateByUrl('home');
    return false;
  }
};

export const authsessionGuardTokenAdmin: CanActivateFn = (route, state) => {
  const router:Router = inject(Router);
  const token = localStorage.getItem('token');
  const helper: JwtHelperService = inject(JwtHelperService);
  if (token) {
    const decodedToken = helper.decodeToken(token);
    if (decodedToken.rol === 'admin'){
      return true;
    }else{
      router.navigateByUrl('home');
      return false;
    }
  } else {
    router.navigateByUrl('home');
    return false;
  }
};

export const authsessionGuardTokenAdminProfeAlum: CanActivateFn = (route, state) => {
  const router:Router = inject(Router);
  const token = localStorage.getItem('token');
  const helper: JwtHelperService = inject(JwtHelperService);
  if (token) {
    const decodedToken = helper.decodeToken(token);
    if (decodedToken.rol === 'admin' || decodedToken.rol === 'profesor'|| decodedToken.rol === 'alumno'){
      return true;
    }else{
      router.navigateByUrl('home');
      return false;
    }
  } else {
    router.navigateByUrl('home');
    return false;
  }
};

export const authsessionGuardTokenAdminProfeAlumEspera: CanActivateFn = (route, state) => {
  const router:Router = inject(Router);
  const token = localStorage.getItem('token');
  const helper: JwtHelperService = inject(JwtHelperService);
  if (token) {
    const decodedToken = helper.decodeToken(token);
    if (decodedToken.rol === 'admin' || decodedToken.rol === 'profesor'|| decodedToken.rol === 'alumno'|| decodedToken.rol === 'espera'){
      return true;
    }else{
      router.navigateByUrl('home');
      return false;
    }
  } else {
    router.navigateByUrl('home');
    return false;
  }
};