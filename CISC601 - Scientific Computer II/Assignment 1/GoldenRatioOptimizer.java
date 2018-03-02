import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.util.function.Function;

public class GoldenRatioOptimizer {
	public static void main(String args[]) {
		System.out.println(
				gold(-2, 4, 100000, 0.01, (x) -> -Math.pow(x, 4) - 2 * Math.pow(x, 3) - 8 * Math.pow(x, 2) - 5 * x));
	}

	@SuppressWarnings("unused")
	static double gold(double xlow, double xhigh, int maxit, double es, Function<Double, Double> f) {
		final double R = (Math.pow(5, 1 / 2.) - 1) / 2;

		double xl = xlow, xu = xhigh;
		int iter = 1;
		double d = R * (xu - xl);
		double x1 = xl + d, x2 = xu - d;
		double f1 = f.apply(x1);
		double f2 = f.apply(x2);
		double ea = 0;

		double xopt, fx;
		if (f1 > f2) {
			xopt = x1;
			fx = f1;
		} else {
			xopt = x2;
			fx = f2;
		}

		do {
			d = R * d;
			double xint = xu - xl;
			if (f1 > f2) {
				xl = x2;
				x2 = x1;
				x1 = xl + d;
				f2 = f1;
				f1 = f.apply(x1);
			} else {
				xu = x1;
				x1 = x2;
				x2 = xu - d;
				f1 = f2;
				f2 = f.apply(x2);
			}
			iter++;
			if (f1 > f2) {
				xopt = x1;
				fx = f1;
			} else {
				xopt = x2;
				fx = f2;
			}

			if (xopt != 0)
				ea = (1 - R) * Math.abs(xint / xopt) * 100;
			if (ea <= es || iter >= maxit)
				break;
		} while (true);

//		DecimalFormat df = new DecimalFormat("#.#####");
//		df.setRoundingMode(RoundingMode.HALF_UP);

//		System.out.println("Error: " + ea);

		return xopt;
	}
}
