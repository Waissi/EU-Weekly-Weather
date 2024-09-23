from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtCharts import *
from PySide6.QtGui import *
from forecast import *
from colorpalette import *


class GraphDisplay(QWidget):
    def __init__(self):
        super().__init__()

        # create the graph
        self.chart = QChart()
        self.chartView = QChartView(self.chart)
        self.spline_series: dict[str, QSplineSeries] = {}

        # create y axis for the temperature
        self.axis_y = QValueAxis()
        self.axis_y.setRange(-15, 35)
        self.axis_y.setTickCount(11)
        self.axis_y.setTitleText("Average Temperature (ºC)")
        self.axis_y.setGridLineVisible(False)

        # create x axis for the week day to come
        self.axis_x = QDateTimeAxis()
        self.axis_x.setFormat("dd MMM yyyy")
        self.axis_x.setTickCount(7)
        startDate = QDateTime()
        startDate.setDate(QDate.currentDate())
        endDate = startDate.addDays(6)
        self.axis_x.setRange(startDate, endDate)
        self.axis_x.setGridLineVisible(False)

        self.chart.setAxisY(self.axis_y)
        self.chart.setAxisX(self.axis_x)

        # apply some style settings to the graph
        plotAreaGradient = QLinearGradient()
        plotAreaGradient.setStart(QPointF(0.5, 1))
        plotAreaGradient.setFinalStop(QPointF(0.5, 0))
        plotAreaGradient.setColorAt(0.0, "white")
        plotAreaGradient.setColorAt(0.3, QColor(173, 216, 230, 220))
        plotAreaGradient.setColorAt(1.0, QColor(255, 165, 0, 100))
        plotAreaGradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        self.chart.setPlotAreaBackgroundBrush(plotAreaGradient)
        self.chart.setPlotAreaBackgroundVisible(True)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.chartView)

    def update(self, city: str):
        """
            Updates the graph when the user chooses a city
        """

        # if the user has already selected the city we just toggle its visibility on the graph
        if city in self.spline_series:
            self.spline_series[city].hide() if self.spline_series[city].isVisible(
            ) else self.spline_series[city].show()
            return

        # fetch the weather data
        city_forecast = get_city_forecast(city)
        if not city_forecast:
            return

        # create the line series from the data and add it to the graph
        new_spline_series = QSplineSeries()
        self.chart.addSeries(new_spline_series)
        color = generate_random_color()
        pen = QPen(color)
        pen.setWidth(4)
        new_spline_series.setPen(pen)
        new_spline_series.attachAxis(self.axis_x)
        new_spline_series.attachAxis(self.axis_y)
        new_spline_series.setName(city)
        for daily_forecast in city_forecast:
            new_spline_series.append(
                daily_forecast.date.toMSecsSinceEpoch(), daily_forecast.average_temp)
        self.spline_series[city] = new_spline_series
