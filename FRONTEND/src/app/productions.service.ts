import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ProductionsService {
  
  //  endpoint obtenir liste des productions
  url = 'http://127.0.0.1:8000/'
  url1 = 'http://127.0.0.1:8000/productions'


   //  endpoint obtenir liste des tâches associées à l'id d'une production

   url2 = 'http://127.0.0.1:8000/get_task_ids_by_production/<int:production_id>/'


  public id :any 

  constructor(private http: HttpClient) { }
  getProductions(): Observable<any[]>{
    return this.http.get<any[]>(this.url+'productions')}


  loadTasksByProductionId(Id: number): Observable<any[]> {
    
    return this.http.get<any[]>(`${this.url}/get_task_ids_by_production/${Id}`)
 }

 loadProducer(): Observable<any[]> {
    
  return this.http.get<any[]>(`${this.url}producer/`)
}





  createNewProduction(formData:any):Observable<any>{
    return this.http.post<any>(`${this.url}change`, formData)
    
 }




}

// getOrganization(organizationId: string): Observable<Organization> {
//   return this.httpClient.get<Organization>(
//               `${this.baseURL}/v1/organizations/${organizationId}`