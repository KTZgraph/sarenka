/*
Podpatrzeć
- https://www.reddit.com/r/dataisbeautiful/comments/e257go/announcing_a_moratorium_on_racing_bar_charts/
- https://www.reddit.com/r/dataisbeautiful/comments/xxa6vl/oc_the_most_popular_attractions_in_top10_most/
- https://www.reddit.com/r/dataisbeautiful/comments/xxqf8a/oc_defense_stocks_have_been_unable_to_hold_onto/
 */

import Navbar from '../../../shared/navbar/Navbar';
import Sidebar from '../../../shared/sidebar/Sidebar';

import TrendsChart from '../components/trends-char/TrendsChart';
import GroupedBarplot from '../components/grouped-barplot/GroupedBarplot';
import BarplotThreeBars from '../components/barplot-three-bars/BarplotThreeBars';

// wykresy kołowe
import PieChartInteractive from '../components/pie-chart-interactive/PieChartInteractive';
import PieChartLabels from '../components/pie-chart-labels/PieChartLabels';

// area charts
import BasicAreaChart from '../components/basic-area-chart/BasicAreaChart';

// heatmap jak github można pokazac natężenie podatności
import CalendarHeatmap from '../components/calendar-heatmap/CalendarHeatmap';

// bazowe pod responswyność i lepsze zażadzanie stanem reacta
import BasicOne from '../components/basic-one/BasicOne';
import BasicOneRemastered from '../components/basic-one-remastered/BasicOneRemastered';
import BasicTwo from '../components/basic-two/BasicTwo';
import BasicThree from '../components/basic-three/BasicThree';
import BasicFour from '../components/basic-four/BasicFour';
import BasicFive from '../components/basic-five/BasicFive';

// łamanie złej linii czasowej
import BreakingBadTimelineApp from '../components/breaking-bad-timeline/BreakingBadTimelineApp';
import RacingBarChartApp from '../components/racing-bar-chart/RacingBarChartApp';
import AnimatedTreeChartApp from '../components/animated-tree-chart/AnimatedTreeChartApp';
import PhysicsBasedForceLayoutApp from '../components/physics-based-force-layout/PhysicsBasedForceLayoutApp';

import './Visualizations.scss';

const VisualizationsRowTrendsChart = () => (
  <div className="visualizations__row">
    <div className="visualizations_col visualizations_col--double-width">
      <div className="visualizations__card">
        <TrendsChart />
      </div>
    </div>
    <div className="visualizations_col">
      <div className="visualizations__card">
        tableka z danymi do podatności na rok + zaznaczenie row
        tabelkii po kliknieciu na słupek
      </div>
    </div>
  </div>
);

const Visualizations = () => {
  return (
    <>
      <Sidebar currentPage="home" />
      <main>
        <Navbar />
        <div className="visualizations">
          <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--full-width">
                <PhysicsBasedForceLayoutApp />
              </div>
            </div>
          </div>

          {/* <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--full-width">
                <AnimatedTreeChartApp />
              </div>
            </div>
          </div> */}

          {/* <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--full-width">
                <RacingBarChartApp />
              </div>
            </div>
          </div> */}

          {/* <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--double-width">
                <BreakingBadTimelineApp />
              </div>
            </div>
            <div className="visualizations_col">
              <div className="visualizations__card">
                <BasicFive />
              </div>
            </div>
          </div> */}

          {/* <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--double-width">
                <BasicFour />
              </div>
            </div>
            <div className="visualizations_col">
              <div className="visualizations__card">
                <BasicThree />
              </div>
            </div>
          </div> */}

          {/* <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--double-width">
                <BasicTwo />
              </div>
            </div>
            <div className="visualizations_col">
              <div className="visualizations__card">
                <BasicOne />
              </div>
            </div>
          </div> */}

          {/* row */}
          {/* <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card">
                <CalendarHeatmap />
              </div>
            </div>
            <div className="visualizations_col">
              <div className="visualizations__card">
                <BasicOneRemastered />
              </div>
            </div>
          </div> */}

          {/* row */}
          {/* <div className="visualizations__row">
            <div className="visualizations_col visualizations_col--double-width">
              <div className="visualizations__card">
                <BasicAreaChart />
              </div>
            </div>
            <div className="visualizations_col">
              <div className="visualizations__card">
                <PieChartLabels />
              </div>
            </div>
          </div> */}

          {/* row */}
          {/* <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card">
                <PieChartInteractive />
              </div>
            </div>
            <div className="visualizations_col">
              <div className="visualizations__card">
                <GroupedBarplot />
              </div>
            </div>
            <div className="visualizations_col">
              <div className="visualizations__card">
                <BarplotThreeBars />
              </div>
            </div>
          </div> */}

          {/* <VisualizationsRowTrendsChart /> */}
        </div>
      </main>
    </>
  );
};

export default Visualizations;
