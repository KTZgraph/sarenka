/*
Podpatrzeć
- https://www.reddit.com/r/dataisbeautiful/comments/e257go/announcing_a_moratorium_on_racing_bar_charts/
- https://www.reddit.com/r/dataisbeautiful/comments/xxa6vl/oc_the_most_popular_attractions_in_top10_most/
- https://www.reddit.com/r/dataisbeautiful/comments/xxqf8a/oc_defense_stocks_have_been_unable_to_hold_onto/
 */

import Navbar from "../../../shared/navbar/Navbar";
import Sidebar from "../../../shared/sidebar/Sidebar";

import TrendsChart from "../components/trends-char/TrendsChart";
import GroupedBarplot from "../components/grouped-barplot/GroupedBarplot";
import BarplotThreeBars from "../components/barplot-three-bars/BarplotThreeBars";

// wykresy kołowe
import PieChartInteractive from "../components/pie-chart-interactive/PieChartInteractive";
import PieChartLabels from "../components/pie-chart-labels/PieChartLabels";

// area charts
import BasicAreaChart from "../components/basic-area-chart/BasicAreaChart";

// heatmap jak github można pokazac natężenie podatności
import CalendarHeatmap from "../components/calendar-heatmap/CalendarHeatmap";

// bazowe pod responswyność i lepsze zażadzanie stanem reacta
import BasicOne from "../components/basic-one/BasicOne";
import BasicOneRemastered from "../components/basic-one-remastered/BasicOneRemastered";
import BasicTwo from "../components/basic-two/BasicTwo";
import BasicThree from "../components/basic-three/BasicThree";
import BasicFour from "../components/basic-four/BasicFour";
import BasicFive from "../components/basic-five/BasicFive";

// łamanie złej linii czasowej
import BreakingBadTimelineApp from "../components/breaking-bad-timeline/BreakingBadTimelineApp";
import RacingBarChartApp from "../components/racing-bar-chart/RacingBarChartApp";
import AnimatedTreeChartApp from "../components/animated-tree-chart/AnimatedTreeChartApp";
// TODO - z tymi siłami jakies dziwne problemy
import PhysicsBasedForceLayoutApp from "../components/physics-based-force-layout/PhysicsBasedForceLayoutApp";

// mapa
import WorldMapApp from "../components/world-map/WorldMapApp";

// filtry po fragmencie wykresu + wykres z podglądem
import FilteringVisuallyApp from "../components/filtering-visually/FilteringVisuallyApp";

// wykresy słupkowe z podziałem kolorystycznym na wysokości
import StackedBarChartApp from "../components/stacked-bar-chart/StackedBarChartApp";

// wykres słupkowy z seriami danych i area chart razem
import StackedAreaChartApp from "../components/stacked-area-chart/StackedAreaChartApp";

// wykres liniowy z opcją zoom
import ZoomableLineChartApp from "../components/zoomable-line-chart/ZoomableLineChartApp";

// rozwiązanie toolipów
import BasicFourTooltip from "../components/basic-four/BasicFourTooltip";

// kołowy wykres
import PieChartNoProblem from "../components/pie-chart-no-problem/PieChartNoProblem";
import DonutChartGroupLabel from "../components/donut-chart-group-label/DonutChartGroupLabel";

// TODO wykres wiele linii
import MultiLineGraphToggle from "../components/multi-line-graph-toggle/MultiLineGraphToggle";

// SimpleBarLineGraph.
import SimpleBarLineGraph from "../components/simple-bar-line-graph/SimpleBarLineGraph";

// hetmapa z tooltipami
import HeatmapTooltip from "../components/heatmap-tooltip/HeatmapTooltip";

import "./Visualizations.scss";

const VisualizationsRowTrendsChart = () => (
  <div className="visualizations__row">
    <div className="visualizations_col visualizations_col--double-width">
      <div className="visualizations__card">
        <TrendsChart />
      </div>
    </div>
    <div className="visualizations_col">
      <div className="visualizations__card">
        tableka z danymi do podatności na rok + zaznaczenie row tabelkii po
        kliknieciu na słupek
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
              <div className="visualizations__card  visualizations_col--double-width"></div>
              <HeatmapTooltip />
            </div>
            <div className="visualizations_col">
              <div className="visualizations__card">
                <SimpleBarLineGraph />
              </div>
            </div>
          </div>

          <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--double-width">
                <MultiLineGraphToggle />
              </div>
            </div>
            <div className="visualizations_col">
              <div className="visualizations__card">
                <DonutChartGroupLabel />
              </div>
            </div>
          </div>

          <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--double-width">
                <PieChartNoProblem />
              </div>
            </div>
            <div className="visualizations_col">
              <div className="visualizations__card">
                <BasicFourTooltip />
              </div>
            </div>
          </div>

          <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--full-width">
                <ZoomableLineChartApp />
              </div>
            </div>
          </div>

          <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--full-width">
                <StackedAreaChartApp />
              </div>
            </div>
          </div>

          <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--full-width">
                <StackedBarChartApp />
              </div>
            </div>
          </div>

          <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--full-width">
                <FilteringVisuallyApp />
              </div>
            </div>
          </div>

          <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--full-width">
                <WorldMapApp />
              </div>
            </div>
          </div>
          <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--full-width">
                <PhysicsBasedForceLayoutApp />
              </div>
            </div>
          </div>
          <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--full-width">
                <PhysicsBasedForceLayoutApp />
              </div>
            </div>
          </div>
          <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--full-width">
                <AnimatedTreeChartApp />
              </div>
            </div>
          </div>
          <div className="visualizations__row">
            <div className="visualizations_col">
              <div className="visualizations__card  visualizations_col--full-width">
                <RacingBarChartApp />
              </div>
            </div>
          </div>
          <div className="visualizations__row">
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
          </div>
          <div className="visualizations__row">
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
          </div>
          <div className="visualizations__row">
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
          </div>
          {/* row */}
          <div className="visualizations__row">
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
          </div>
          {/* row */}
          <div className="visualizations__row">
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
          </div>
          {/* row */}
          <div className="visualizations__row">
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
          </div>
          <VisualizationsRowTrendsChart />
        </div>
      </main>
    </>
  );
};

export default Visualizations;
