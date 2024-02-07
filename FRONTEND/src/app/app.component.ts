import { Component, OnInit } from '@angular/core';


import { NewComponent } from './new/new.component';
import { ProductionsComponent } from './productions/productions.component';


import { RouterOutlet } from '@angular/router';

import { routes } from './app.routes';

import { ProductionsService } from './productions.service';

import { HttpClientModule } from '@angular/common/http';

import { NgFor } from '@angular/common';

import { RouterLink } from '@angular/router';

import { ProductionIdTtaskComponent } from './production-id-ttask/production-id-ttask.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, NewComponent,ProductionsComponent,HttpClientModule,NgFor,ProductionIdTtaskComponent],
  providers: [ProductionsService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {

  

    title = 'testservice3';
  }





