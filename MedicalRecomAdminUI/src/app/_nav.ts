export interface NavData {
  name?: string;
  url?: string;
  icon?: string;
  badge?: any;
  title?: boolean;
  children?: any;
  variant?: string;
  attributes?: object;
  divider?: boolean;
  class?: string;
}

export const navItems: NavData[] = [
  {
    name: 'Dashboard',
    url: '/dashboard',
    icon: 'icon-speedometer'
  },
  {
        name: 'Users',
        url: '/base/users',
        icon: 'icon-puzzle'
  },
  {
        name: 'Drugs',
        url: '/base/drugs',
        icon: 'icon-puzzle'
  },
  {
        name: 'Response',
        url: '/base/responses',
        icon: 'icon-puzzle'
  },
  {
        name: 'Hashtags',
        url: '/base/hashtags',
        icon: 'icon-puzzle'
  },
  {
        name: 'Conversation',
        url: '/base/conversation',
        icon: 'icon-puzzle'
  }
];
