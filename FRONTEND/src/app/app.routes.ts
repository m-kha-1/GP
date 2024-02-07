import { Routes } from '@angular/router';
import { NewComponent } from './new/new.component';
import { ProductionsComponent } from './productions/productions.component';
import { ProductionIdtasksComponent } from './production-idtasks/production-idtasks.component';
import { AddformComponent } from './addform/addform.component';
export const routes: Routes = [

    {path:'new', component: NewComponent},
    {path:'productions', component: ProductionsComponent},
    {path:'productionsIdTasks', component:ProductionIdtasksComponent },
    {path:'add', component:AddformComponent },
];
