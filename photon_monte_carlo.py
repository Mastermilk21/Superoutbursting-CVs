import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def photon_scattering_simulation(tau, num_photons=100000):
    """
    Monte Carlo simulation of photon scattering in a medium with optical depth tau.
    
    Parameters:
    tau (float): Optical depth of the medium
    num_photons (int): Number of photons to simulate
    
    Returns:
    tuple: (mean_scatterings, scattering_counts, escape_probabilities)
    """
    
    scattering_counts = []
    
    for i in range(num_photons):
        # Initialize photon at the center of the medium (position = 0)
        # Medium extends from -tau/2 to +tau/2
        position = 0.0
        scatterings = 0
        
        while True:
            # Calculate distance to next scattering event
            # In a medium with optical depth, the mean free path is 1
            # Distance to next scattering follows exponential distribution
            distance_to_scatter = np.random.exponential(1.0)
            
            # Choose random direction (inward or outward with equal probability)
            direction = np.random.choice([-1, 1])
            
            # Calculate new position after scattering
            new_position = position + direction * distance_to_scatter
            
            # Check if photon escapes the medium
            if abs(new_position) >= tau/2:
                # Photon escapes without this scattering
                break
            else:
                # Photon scatters within the medium
                position = new_position
                scatterings += 1
                
                # Safety check to prevent infinite loops
                if scatterings > 10000:
                    break
        
        scattering_counts.append(scatterings)
        
        # Progress indicator
        if (i + 1) % 10000 == 0:
            print(f"Simulated {i + 1} photons...")
    
    mean_scatterings = np.mean(scattering_counts)
    
    return mean_scatterings, scattering_counts

def theoretical_calculation(tau):
    """
    Theoretical calculation for comparison.
    For a slab geometry with optical depth tau, the expected number of scatterings
    can be approximated analytically.
    """
    # For a symmetric random walk in a slab, the theoretical expectation
    # is approximately tau^2/4 for large tau
    return tau**2 / 4

def analyze_results(tau, mean_scatterings, scattering_counts):
    """
    Analyze and visualize the simulation results.
    """
    print(f"\n=== PHOTON SCATTERING SIMULATION RESULTS ===")
    print(f"Optical depth (τ): {tau}")
    print(f"Number of photons simulated: {len(scattering_counts)}")
    print(f"Mean number of scatterings: {mean_scatterings:.3f}")
    print(f"Standard deviation: {np.std(scattering_counts):.3f}")
    print(f"Median number of scatterings: {np.median(scattering_counts):.3f}")
    
    # Theoretical comparison
    theoretical = theoretical_calculation(tau)
    print(f"Theoretical approximation (τ²/4): {theoretical:.3f}")
    print(f"Difference from theory: {abs(mean_scatterings - theoretical):.3f}")
    
    # Statistical analysis
    print(f"\nStatistical Analysis:")
    print(f"Minimum scatterings: {min(scattering_counts)}")
    print(f"Maximum scatterings: {max(scattering_counts)}")
    print(f"95% confidence interval: [{np.percentile(scattering_counts, 2.5):.1f}, {np.percentile(scattering_counts, 97.5):.1f}]")
    
    # Create histogram
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.hist(scattering_counts, bins=50, density=True, alpha=0.7, edgecolor='black')
    plt.axvline(mean_scatterings, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_scatterings:.3f}')
    plt.axvline(theoretical, color='green', linestyle='--', linewidth=2, label=f'Theory: {theoretical:.3f}')
    plt.xlabel('Number of Scatterings')
    plt.ylabel('Probability Density')
    plt.title(f'Distribution of Scatterings (τ = {tau})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Cumulative distribution
    plt.subplot(2, 2, 2)
    sorted_counts = np.sort(scattering_counts)
    cumulative_prob = np.arange(1, len(sorted_counts) + 1) / len(sorted_counts)
    plt.plot(sorted_counts, cumulative_prob, linewidth=2)
    plt.axvline(mean_scatterings, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_scatterings:.3f}')
    plt.xlabel('Number of Scatterings')
    plt.ylabel('Cumulative Probability')
    plt.title('Cumulative Distribution Function')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Log-scale histogram for better visualization of tail
    plt.subplot(2, 2, 3)
    plt.hist(scattering_counts, bins=50, density=True, alpha=0.7, edgecolor='black')
    plt.yscale('log')
    plt.axvline(mean_scatterings, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_scatterings:.3f}')
    plt.xlabel('Number of Scatterings')
    plt.ylabel('Log Probability Density')
    plt.title('Distribution (Log Scale)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Box plot
    plt.subplot(2, 2, 4)
    plt.boxplot(scattering_counts, vert=True)
    plt.ylabel('Number of Scatterings')
    plt.title('Box Plot of Scatterings')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def run_multiple_tau_analysis():
    """
    Run simulation for multiple optical depths to see the scaling behavior.
    """
    tau_values = [1, 2, 3, 4, 5, 6, 7, 8]
    mean_scatterings_list = []
    theoretical_list = []
    
    print("\n=== SCALING ANALYSIS ===")
    print("τ\tSimulated\tTheoretical\tRatio")
    print("-" * 40)
    
    for tau in tau_values:
        mean_scatterings, _ = photon_scattering_simulation(tau, num_photons=50000)
        theoretical = theoretical_calculation(tau)
        
        mean_scatterings_list.append(mean_scatterings)
        theoretical_list.append(theoretical)
        
        ratio = mean_scatterings / theoretical if theoretical > 0 else 0
        print(f"{tau}\t{mean_scatterings:.3f}\t\t{theoretical:.3f}\t\t{ratio:.3f}")
    
    # Plot scaling behavior
    plt.figure(figsize=(10, 6))
    plt.plot(tau_values, mean_scatterings_list, 'bo-', linewidth=2, markersize=8, label='Monte Carlo Simulation')
    plt.plot(tau_values, theoretical_list, 'r--', linewidth=2, label='Theoretical (τ²/4)')
    plt.xlabel('Optical Depth (τ)')
    plt.ylabel('Mean Number of Scatterings')
    plt.title('Scaling of Mean Scatterings with Optical Depth')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    # Main simulation for τ = 5
    tau = 5
    print(f"Running Monte Carlo simulation for optical depth τ = {tau}")
    print("This may take a few moments...")
    
    mean_scatterings, scattering_counts = photon_scattering_simulation(tau, num_photons=100000)
    
    # Analyze results
    analyze_results(tau, mean_scatterings, scattering_counts)
    
    # Run scaling analysis
    run_multiple_tau_analysis()
    
    print(f"\n=== FINAL ANSWER ===")
    print(f"For optical depth τ = {tau}:")
    print(f"Expected number of scatterings: {mean_scatterings:.3f}")




