import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ComponentCommunicatorService {
  private data: any;

  constructor() { }

  setData(data: any): void {
    this.data = data;
    // this.data = data[0];
  }

  getData(): any {
    return this.data;
  }
}

