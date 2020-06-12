#include "TCanvas.h"
#include "TROOT.h"
#include "TGraphErrors.h"
#include "TF1.h"
#include "TLegend.h"
#include "TArrow.h"
#include "TLatex.h"
#include <vector>

void press1()
{
    std::vector<double> x_vals =
        {0.05263158, 0.10526316, 0.15789474, 0.21052632,
         0.26315789, 0.31578947, 0.36842105, 0.42105263, 0.47368421,
         0.52631579, 0.57894737, 0.63157895, 0.68421053, 0.73684211,
         0.78947368, 0.84210526, 0.89473684, 0.94736842, 1.};
    std::vector<double> y_vals =
        {0.04405152463590652,
         0.06090324266926067,
         0.1978139134528996,
         0.15570544869865263,
         0.16482988564076576,
         0.23783384882536343,
         0.2344795644462567,
         0.03233471420955825,
         0.5116441277309157,
         0.5500577602718167,
         0.6897845211361802,
         0.764815766765245,
         1.8738583481619606,
         1.330717051225428,
         2.5705872437942783,
         4.824495695967393,
         6.500839662796084,
         12.105228868979317,
         19.088537825160426};
    std::vector<double> y_errs =
        {0.00147676, 0.00622644, 0.02894447, 0.01833997, 0.04831321,
         0.04601449, 0.04983224, 0.0630486, 0.05904223, 0.03024967,
         0.0478519, 0.0337484, 0.11512486, 0.03998229, 0.07334786,
         0.03092993, 0.07749556, 0.04662986, 0.03257229};

    // Instance of the graph
    TGraphErrors graph(x_vals.size(), &x_vals[0], &y_vals[0], nullptr, &y_errs[0]);
    graph.SetTitle("; 1/N; Total Energy");
    // Make the plot estetically better
    graph.SetMarkerStyle(kOpenCircle);
    graph.SetMarkerColor(kBlue);
    graph.SetLineColor(kBlue);
    // auto func = new TF1("func", "[0]*TMath::Power(x, [1])", 0, 1);
    // func->SetParameter(0, -10);
    // func->SetParameter(1, -0.5);
    // graph.Fit(func);
    // The canvas on which we'll draw the graph
    auto mycanvas = new TCanvas();
    // auto leg = new TLegend(.1, .7, .3, .9);
    // leg->AddEntry(&graph, "Results");
    // leg->AddEntry(func, "Fit");
    // mycanvas->SetLogy();
    // mycanvas->SetLogx();
    // Draw the graph !
    graph.DrawClone("APEL");
    // leg->DrawClone("Same");

    // mycanvas->Print("fit_exp1_p.eps");
}

// int main()
// {
//     macro1();
// }
