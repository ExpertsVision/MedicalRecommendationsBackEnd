import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CardsComponent } from './cards.component';
import { FormsComponent } from './forms.component';
import { CarouselsComponent } from './carousels.component';
import { CollapsesComponent } from './collapses.component';
import { PaginationsComponent } from './paginations.component';

const routes: Routes = [
  {
    path: '',
    data: {
      title: 'Base'
    },
    children: [
      
      {
        path: 'users',
        component: CardsComponent,
        data: {
          title: 'Users'
        }
      },
      {
        path: 'drugs',
        component: CarouselsComponent,
        data: {
          title: 'Drugs'
        }
      },
      {
        path: 'responses',
        component: CollapsesComponent,
        data: {
          title: 'Responses'
        }
      },
       {
        path: 'conversation',
        component: PaginationsComponent,
        data: {
          title: 'Conversation'
        }
      },
      {
        path: 'hashtags',
        component: FormsComponent,
        data: {
          title: 'Hashtags'
        }
      },
     
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BaseRoutingModule {}
