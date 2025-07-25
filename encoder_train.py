from utils.argutils import print_args
from encoder.train import train
from pathlib import Path
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Trains the speaker encoder. You must have run encoder_preprocess.py first.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("run_id", type=str, help= \
        "Name for this model. By default, training outputs will be stored to saved_models/<run_id>/. If a model state "
        "from the same run ID was previously saved, the training will restart from there. Pass -f to overwrite saved "
        "states and restart from scratch.")
    parser.add_argument("clean_data_root", type=Path, help= \
        "Path to the output directory of encoder_preprocess.py. If you left the default "
        "output directory when preprocessing, it should be <datasets_root>/SV2TTS/encoder/.")
    parser.add_argument("-m", "--models_dir", type=Path, default="saved_models", help=\
        "Path to the root directory that contains all models. A directory <run_name> will be created under this root."
        "It will contain the saved model weights, as well as backups of those weights and plots generated during "
        "training.")
    parser.add_argument("-v", "--vis_every", type=int, default=10, help= \
        "Number of steps between updates of the loss and the plots.")
    parser.add_argument("-u", "--umap_every", type=int, default=0, help= \
        "Number of steps between updates of the umap projection. Set to 0 to never update the "
        "projections.")
    parser.add_argument("-s", "--save_every", type=int, default=10, help= \
        "Number of steps between updates of the model on the disk. Set to 0 to never save the "
        "model.")
    parser.add_argument("-b", "--backup_every", type=int, default=10, help= \
        "Number of steps between backups of the model. Set to 0 to never make backups of the "
        "model.")
    parser.add_argument("-f", "--force_restart", action="store_true", help= \
        "Do not load any saved model.")
    parser.add_argument("--visdom_server", type=str, default="http://localhost")
    parser.add_argument("--no_visdom", action="store_true", help= \
        "Disable visdom.")

    args = parser.parse_args()



    # Run the training
    print_args(args, parser)
    train(**vars(args))


# from utils.argutils import print_args
# from encoder.train import train
# from pathlib import Path
# import argparse

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         description="Trains the speaker encoder. You must have run encoder_preprocess.py first.",
#         formatter_class=argparse.ArgumentDefaultsHelpFormatter
#     )
#     parser.add_argument("run_id", type=str, help=
#         "Name for this model. By default, training outputs will be stored to saved_models/<run_id>/. If a model state "
#         "from the same run ID was previously saved, the training will restart from there. Pass -f to overwrite saved "
#         "states and restart from scratch.")
#     parser.add_argument("clean_data_root", type=Path, help=
#         "Path to the output directory of encoder_preprocess.py. If you left the default "
#         "output directory when preprocessing, it should be <datasets_root>/SV2TTS/encoder/.")
#     parser.add_argument("-m", "--models_dir", type=Path, default="saved_models", help=
#         "Path to the root directory that contains all models. A directory <run_name> will be created under this root."
#         "It will contain the saved model weights, as well as backups of those weights and plots generated during "
#         "training.")
#     parser.add_argument("-v", "--vis_every", type=int, default=50, help=
#         "Number of steps between updates of the loss and the plots.")
#     parser.add_argument("-u", "--umap_every", type=int, default=0, help=
#         "Number of steps between updates of the umap projection. Set to 0 to never update the "
#         "projections.")
#     parser.add_argument("-s", "--save_every", type=int, default=50, help=
#         "Number of steps between updates of the model on the disk. Set to 0 to never save the "
#         "model.")
#     parser.add_argument("-b", "--backup_every", type=int, default=0, help=
#         "Number of steps between backups of the model. Set to 0 to never make backups of the "
#         "model.")
#     parser.add_argument("-f", "--force_restart", action="store_true", help=
#         "Do not load any saved model.")
#     parser.add_argument("--visdom_server", type=str, default="http://localhost")
#     parser.add_argument("--no_visdom", action="store_true", help=
#         "Disable visdom.")
#     parser.add_argument("--max_steps", type=int, default=3600, help=
#         "Maximum number of training steps to run. Set to 0 to run until convergence.")

#     args = parser.parse_args()

#     print_args(args, parser)
#     train(**vars(args))
