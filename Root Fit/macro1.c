#include "TCanvas.h"
#include "TROOT.h"
#include "TGraphErrors.h"
#include "TF1.h"
#include "TLegend.h"
#include "TArrow.h"
#include "TLatex.h"
#include <vector>

void macro1()
{
    std::vector<double> x_vals =
        {0.01,
         0.00909090909090909,
         0.008333333333333333,
         0.007692307692307693,
         0.007142857142857143,
         0.006666666666666667,
         0.00625,
         0.0058823529411764705,
         0.005555555555555556,
         0.005263157894736842,
         0.005};
    std::vector<double> y_vals =
        {-240.58335040740437,
         -261.1081311056638,
         -280.5409638461601,
         -309.03578722500936,
         -330.50375905764315,
         -358.54904766085787,
         -384.1436239542724,
         -403.7990735756446,
         -425.9943502200832,
         -456.8859362447672,
         -473.90995060003445};
    std::vector<double> y_errs =
        {4.00769149, 5.50982799, 5.83413919, 7.72521482, 6.00075762,
         6.37212228, 7.04240594, 8.61068864, 6.03640031, 6.82575498,
         6.99046487};

    // Instance of the graph
    TGraphErrors graph(x_vals.size(), &x_vals[0], &y_vals[0], nullptr, &y_errs[0]);
    graph.SetTitle("; 1/N; Total Energy");
    // Make the plot estetically better
    graph.SetMarkerStyle(kOpenCircle);
    graph.SetMarkerColor(kBlue);
    graph.SetLineColor(kBlue);
    auto func = new TF1("func", "[0]*TMath::Power(x, [1])", 0, 1);
    func->SetParameter(0, -10);
    func->SetParameter(1, -0.5);
    graph.Fit(func);
    // The canvas on which we'll draw the graph
    auto mycanvas = new TCanvas();
    auto leg = new TLegend(.1, .7, .3, .9);
    leg->AddEntry(&graph, "Results");
    leg->AddEntry(func, "Fit");
    // mycanvas->SetLogy();
    // mycanvas->SetLogx();
    // Draw the graph !
    graph.DrawClone("APEL");
    leg->DrawClone("Same");

    mycanvas->Print("fit_exp1_p.eps");
}

int main()
{
    macro1();
}
