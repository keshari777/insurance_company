import React from "react";
import { Bar } from "@ant-design/plots";

const Visualization = ({ data }) => {
  /**
   *This component is used to display bar chart
   * */
  const config = {
    data,
    xField: "count",
    yField: "month",
    seriesField: "month",
    legend: {
      position: "top-left",
    },
    yAxis: {
      title: {
        text: "Month",
      },
    },
    xAxis: {
      title: {
        text: "Count",
      },
    },
  };
  return <Bar {...config} />;
};

export default Visualization;
