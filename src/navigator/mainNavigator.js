import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import Settings178694Navigator from '../features/Settings178694/navigator';
import Settings178356Navigator from '../features/Settings178356/navigator';
import Settings178339Navigator from '../features/Settings178339/navigator';
import Messaging37178336Navigator from '../features/Messaging37178336/navigator';
import Settings178318Navigator from '../features/Settings178318/navigator';
import Settings178125Navigator from '../features/Settings178125/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
Settings178694: { screen: Settings178694Navigator },
Settings178356: { screen: Settings178356Navigator },
Settings178339: { screen: Settings178339Navigator },
Messaging37178336: { screen: Messaging37178336Navigator },
Settings178318: { screen: Settings178318Navigator },
Settings178125: { screen: Settings178125Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
