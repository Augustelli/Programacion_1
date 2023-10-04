import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, take } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  url='http://127.0.0.1:5002';

  constructor(
    private httpClient: HttpClient
  ) { }
  login ():Observable<any>{
    let dataLogin = {email:'admin@example.com', contrasegna:'admin'};
    return this.httpClient.post(this.url+'/auth/login_two',dataLogin).pipe(take(1));
  }
}
