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


export const authsessionGuardTokenAdminUser: CanActivateFn = (route, state) => {
  const router:Router = inject(Router);
  const token = localStorage.getItem('token');
  const helper: JwtHelperService = inject(JwtHelperService);
  if (token) {
    const decodedToken = helper.decodeToken(token);
    if (decodedToken.role === 'admin' || decodedToken.role === 'user'){
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

